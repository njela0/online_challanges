export function fizzbuzz(number) {
  const result = [];

  for (let i = 1; i <= number; i++) {
    let output = "";

    if (i % 3 === 0) output += "Fizz";
    if (i % 5 === 0) output += "Buzz";

    const value = output || i;

    console.log(value);      // Ausgabe für dich
    result.push(value);      // Rückgabe für Tests
  }

  return result;
}