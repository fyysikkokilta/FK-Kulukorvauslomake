module.exports = {
    lintOnSave: false,

    devServer: {
        proxy: {
            '/api': {
                target: 'http://localhost:8000',
                pathRewrite: {
                    '^/api': '',
                },
            },
        },
    },

    pluginOptions: {
        'style-resources-loader': {
            preProcessor: 'scss',
            patterns: [],
        },
    },
};
