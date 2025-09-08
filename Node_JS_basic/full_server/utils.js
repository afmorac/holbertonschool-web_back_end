import { readFile } from 'fs';

export default function readDatabase(path) {
  return new Promise((resolve, reject) => {
    readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(err);
        return;
      }
      const lines = data
        .trim()
        .split('\n')
        .filter((line) => line.trim() !== '');

      const rows = lines.slice(1);
      const byField = {};

      rows.forEach((line) => {
        const parts = line.split(',');
        if (parts.length >= 4) {
          const firstname = parts[0].trim();
          const field = parts[3].trim();
          if (!byField[field]) byField[field] = [];
          byField[field].push(firstname);
        }
      });

      resolve(byField);
    });
  });
}
