module.exports = {
  name: 'dev',
  description: 'A developer command',
  execute(message, args) {
    if (message.author.id === 'your-discord-user-id') {
      message.reply('You are a developer!');
    } else {
      message.reply('You are not a developer.');
    }
  },
};
