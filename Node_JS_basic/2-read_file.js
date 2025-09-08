const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data
      .trim()
      .split('\n')
      .filter((line) => line.trim() !== ''); // eliminar líneas vacías

    const students = lines.slice(1);

    const numberOfStudents = students.length;
    console.log(`Number of students: ${numberOfStudents}`);

    const fields = {};

    students.forEach((line) => {
      const parts = line.split(',');
      const firstname = parts[0].trim();
      const field = parts[3].trim();

      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    });

    Object.keys(fields).forEach((field) => {
      const list = fields[field].join(', ');
      console.log(
        `Number of students in ${field}: ${fields[field].length}. List: ${list}`,
      );
    });
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
