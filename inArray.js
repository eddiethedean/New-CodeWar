function inArray(array1,array2){
    var len = array1.length;
    var s2 = array2.join(" ");
    var tempArray = [];
    for (var i=0;i<len;i++) {
      if (array1[i]!=undefined&&s2.search(array1[i])!=-1) {
        tempArray.push(array1[i]);
      }
    }
    return tempArray.sort()
  }
  