function catMouse(x){
  var cat_i = x.indexOf('C');
  var mou_i = x.indexOf('m');
  if (mou_i - cat_i <= 4) {
    return "Caught!"
  }
  else {
    return "Escaped!"
  }
}