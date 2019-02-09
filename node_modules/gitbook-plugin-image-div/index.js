module.exports = {

    // Map of hooks
    hooks: {
      "page:before": function(page) {
        page.content = page.content.replace(/<div class=\"image\">/g, '-div-')
            .replace(/<\/div>/g, '-/div-');
        return page;
      }
      ,
      "page": function(page) {
        page.content = page.content.replace(/<p>-div-<\/p>/g, '<div class="image">')
            .replace(/<p>-\/div-<\/p>/g, '</div>');
        return page;
      }
    },

    // Map of new blocks
    blocks: {},

    // Map of new filters
    filters: {}
};
