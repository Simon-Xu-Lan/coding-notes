// @ADD YOUR CODE HERE

d3.select('body').on('change', updatePage);

function updatePage() {
  var dropDownMenu = d3.selectAll('#selectOption').node();
  var dropDownMenuId = dropDownMenu.id;
  var selectOption = dropDownMenu.value;

  console.log(dropDownMenuId);
  console.log(selectOption);
}
