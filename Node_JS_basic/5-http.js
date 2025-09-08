const http = require('http');
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

      const students = lines.slice(1); // quita header

      const fields = {};
      students.forEach((line) => {
        const parts = line.split(',');
        const firstname = parts[0].trim();
        const field = parts[3].trim();
        if (!fields[field]) fields[field] = [];
        fields[field].push(firstname);
      });

      const total = students.length;
      const out = [];
      out.push(`Number of students: ${total}`);

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

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
    return;
  }

  if (req.url === '/students') {
    const header = 'This is the list of our students';
    buildStudentsReport(dbPath)
      .then((report) => {
        res.end(`${header}\n${report}`);
      })
      .catch((e) => {
        res.end(`${header}\n${e.message}`);
      });
    return;
  }

  res.end('Hello Holberton School!');
});

app.listen(1245);

module.exports = app;
