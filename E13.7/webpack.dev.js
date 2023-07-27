const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');

module.exports = merge(common, {
    mode: 'development',
    devtool: 'inline-source-map',
    devServer: {
        static: './dist',
        hot: true,
        devMiddleware: {
            stats: {
                children: false,
                maxModules: 0,
            },
        },
        // headers: {
        //     'Access-Control-Allow-Origin': '*',
        //     'Access-Control-Allow-Methods':
        //         'GET, POST, PUT, DELETE, PATCH, OPTIONS',
        //     'Access-Control-Allow-Headers':
        //         'X-Requested-With, content-type, Authorization',
        // },
        proxy: {
            '/api': {
                target: 'http://localhost:3010',
                pathRewrite: { '^/api': '' },
            },
        },
    },
});
