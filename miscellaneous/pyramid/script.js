const character = "!";
const count = 10;
const rows = [];

let inverted = false;

function padRow(rowNumber, rowCount) {
    return (" ").repeat(rowCount - rowNumber) + character.repeat(2 * rowNumber - 1) + (" ").repeat(rowCount - rowNumber);
}

/* for (let i = 1; i <= count; i++) {
    rows.push(padRow(i, count));
} */

for (let i = 1; i <= count; i++) {
    if (inverted) {
        rows.unshift(padRow(i, count));
    } else {
        rows.push(padRow(i, count));
    }
}

/* while (rows.length < count) {
    rows.push(padRow(rows.length + 1, count));
} */

/* for (let i = count; i > 0; i--) {
    rows.push(padRow(i, count));
} */

/* if (true) {
    console.log("Condition is true");
}

let result = "";

for (const row of rows) {
    result = result + row + "\n";
} */