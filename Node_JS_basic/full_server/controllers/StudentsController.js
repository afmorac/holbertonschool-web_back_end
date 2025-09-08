import readDatabase from '../utils.js';

class StudentsController {
  static async getAllStudents(req, res) {
    const dbPath = process.argv[2];
    res.set('Content-Type', 'text/plain');

    try {
      const byField = await readDatabase(dbPath);
      const header = 'This is the list of our students';
      const lines = [header];

      Object.keys(byField)
        .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()))
        .forEach((field) => {
          const list = byField[field] || [];
          lines.push(
            `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`
          );
        });

      res.status(200).send(lines.join('\n'));
    } catch (e) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const dbPath = process.argv[2];
    const { major } = req.params;
    res.set('Content-Type', 'text/plain');

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const byField = await readDatabase(dbPath);
      const list = byField[major] || [];
      res.status(200).send(`List: ${list.join(', ')}`);
    } catch (e) {
      res.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController;
