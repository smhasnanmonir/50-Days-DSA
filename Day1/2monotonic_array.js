function monotonic_array(a) {
  array_length = a.length;
  first_number = a[0];
  last_number = a[array_length - 1];

  if (first_number < last_number) {
    for (let i = 0; i < array_length - 1; i++) {
      if (a[i] > a[i + 1]) {
        return false;
      }
    }
  } else if (first_number == last_number) {
    for (let i = 0; i < array_length - 1; i++) {
      if (a[i] != a[i + 1]) {
        return false;
      }
    }
  } else {
    for (let i = 0; i < array_length - 1; i++) {
      if (a[i] < a[i + 1]) {
        return false;
      }
    }
  }
  return true;
}

console.log(monotonic_array([3, 4, 6]));
console.log(monotonic_array([3, 3, 3]));
console.log(monotonic_array([3, 1, -3]));
console.log(monotonic_array([3, 1, -3, 2]));
