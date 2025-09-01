module.exports = {
    env: { browser: false, es2021: true, jest: true, node: true },
    extends: ['eslint:recommended'],
    parserOptions: { ecmaVersion: 'latest', sourceType: 'module' },
    rules: {
      'no-unused-vars': ['warn'],
      'no-console': 'off',
    },
  };
  