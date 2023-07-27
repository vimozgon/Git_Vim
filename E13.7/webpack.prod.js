const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');
// const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');
const TerserWebpackPlugin = require('terser-webpack-plugin');

module.exports = merge(common, {
    mode: 'production',
    //   plugins: [new MiniCssExtractPlugin()],
    optimization: {
        minimizer: [new TerserWebpackPlugin({}), new CssMinimizerPlugin({})],
    },
});
