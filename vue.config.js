module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
  ? '/dbms-pd-maker/'
  : '/',
  transpileDependencies: [
    'vuetify'
  ],
}
