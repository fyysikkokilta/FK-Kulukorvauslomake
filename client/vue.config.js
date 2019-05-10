module.exports = {
  lintOnSave: false,

  devServer: {
    disableHostCheck: true,
  },

  pluginOptions: {
    'style-resources-loader': {
      preProcessor: 'scss',
      patterns: [],
    },
  },
  chainWebpack: (config) => {
    config.resolve.symlinks(false)
  },
};
