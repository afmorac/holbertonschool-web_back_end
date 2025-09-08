const express = require('express');
const fs = require('fs');

function buildStudentsReport(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data
        .trim()
        .split('\n')
        .filter((line) => line.trim() !== '');

      const students = lines.slice(1); // quitar header

      const fields = {};
      students.forEach((line) => {
        const parts = line.split(',');
        const firstname = parts[0].trim();
        const field = parts[3].trim();
        if (!fields[field]) fields[field] = [];
        fields[field].push(firstname);
      });

      const out = [];
      out.push(`Number of students: ${students.length}`);

      Object.keys(fields)
        .sort()
        .forEach((field) => {
          out.push(
            `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`
          );
        });

      resolve(out.join('\n'));
    });
  });
}

const dbPath = process.argv[2];
const app = express();

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.set('Content-Type', 'text/plain');
  const header = 'This is the list of our students';
  buildStudentsReport(dbPath)
    .then((report) => res.send(`${header}\n${report}`))
    .catch((e) => res.send(`${header}\n${e.message}`));
});

app.listen(1245);

module.exports = app;
