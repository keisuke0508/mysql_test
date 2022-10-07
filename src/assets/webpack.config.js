const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');

module.exports = {
  mode: "development",
  watch: true,
  entry: './scss/style.scss',
  output: {
    path: path.join(__dirname, '../dist'),
    filename: 'index.js',
  },
  module: {
    rules: [
      {
        test: /\.scss/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          'sass-loader',
        ]
      }
    ]
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: './style.css',
    })
  ],
  optimization: {
    minimizer: [
      new CssMinimizerPlugin()
    ]
  },
  target: ["web", "es5"],
};