module.exports = {
  devServer: {
    proxy: {
      '^/api/': {
          target: 'http://localhost:5000/',
          ws: true,
          changeOrigin: true,
      },
    },
    disableHostCheck: true,
  },
  publicPath: '',
  "transpileDependencies": [
    "vuetify"
  ],
  configureWebpack: {
    devtool: 'source-map'
  }
}