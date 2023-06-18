module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? '/Autonomous_AI_Dialogues/'
    : '/',
  chainWebpack: (config) => {
    config.module.rules.delete("eslint");
  },
};
