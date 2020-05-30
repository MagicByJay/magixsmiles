module.exports = function(eleventyConfig) {
  // copy extra site files to output direcotry

  eleventyConfig.addPassthroughCopy({ "frontend/reveal": "reveal" });
};