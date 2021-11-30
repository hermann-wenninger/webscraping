function printDOM(node, prefix) {
  console.log(prefix + node.nodeName);
  for (let i = 0; i < node.childNodes.length; i++) {
    printDOM(node.childNodes[i], prefix + "\t");
  }
}
printDOM(document, "");

//treewalker object
var treeWalker = document.createTreeWalker(
  document,
  NodeFilter.SHOW_ALL,
  {
    acceptNode: function (node) {
      return NodeFilter.FILTER_ACCEPT;
    },
  },
  false
);

var nodeList = [];
var currentNode = treeWalker.currentNode;
console.log('treewalker-object:', nodeList)

while (currentNode) {
  nodeList.push(currentNode);
  currentNode = treeWalker.nextNode();

}