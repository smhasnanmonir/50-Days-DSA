function kth_symbol(num, k) {
  let total_len = 2 ** (num - 1);
  let mid_value = Math.floor(total_len / 2);
  if (k > total_len) {
    return "invalid";
  }

  if (num == 1) {
    return 0;
  } else if (k <= mid_value) {
    return kth_symbol(num - 1, k);
  } else {
    return 1 - kth_symbol(num - 1, k - mid_value);
  }
}

console.log(kth_symbol(4, 7));
console.log(kth_symbol(4, 8));
console.log(kth_symbol(4, 9));
