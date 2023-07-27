const HtmlWebpackPlugin = require("html-webpack-plugin");
module.exports = {
    mode: "development",
    entry: "./src/index.js",
    devtool: "inline-source-map",
    devServer: {
        static: "./dist",
        hot: true,
        devMiddleware: {
            stats: {
                children: false,
                maxModules: 0,
            },
        },
    },
    plugins: [
        new HtmlWebpackPlugin({
            title: "Development",
        }),
    ],
    output: {
        filename: "main.js",
    },
};
