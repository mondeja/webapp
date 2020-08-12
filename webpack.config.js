'use strict'

const path = require('path');

// NODE_ENV environment variable exists? if staging production else NODE_ENV
// ENV environment variable exists? if staging production else ENV or development
const ENV = process.env.NODE_ENV == 'staging' ? 'production' : (
  process.env.NODE_ENV ? process.env.NODE_ENV : (
    process.env.ENV == 'staging' ? 'production' : (
      process.env.ENV ? process.env.NODE_ENV : 'development')
  )
);

module.exports = {
  mode: ENV,
  entry: path.resolve('frontend', 'src', 'js', 'app01', 'index.js'),
  output: {
    path: path.resolve('frontend', 'dist', 'js', 'app01'),
    filename: '[name].js'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-react']
          }
        }
      }
    ]
  }
}
