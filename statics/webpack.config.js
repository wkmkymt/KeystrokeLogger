const path = require("path");

const pathes = {
  src:  path.resolve(__dirname, "src"),
  dist: path.resolve(__dirname, "dist")
}

module.exports = {
  mode: "development",
  devtool: "inline-source-map",

  context: pathes.src,
  entry: [
    "./index.jsx"
  ],

  output: {
    path: pathes.dist,
    filename: "./js/keystroke.js"
  },

  module: {
    rules: [
      {
        test: /\.jsx$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  },

  devServer: {
    contentBase: pathes.dist,
    publicPath: "/",
    open: true,
    port: 3000
  },

  resolve: {
    extensions: [".js", ".jsx"]
  }

};
