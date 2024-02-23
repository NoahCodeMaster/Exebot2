module.exports = {
  name: 'dev',
  description: 'A developer command',
  execute(message, args) {
    if (message.author.id === '842201757948968991') {
      message.reply('You are a developer!');
    } else {
      message.reply('You are not a developer.');
    }
  },
};
