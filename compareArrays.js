function comp(array1, array2) {
    if (array1===null || array2===null) {
        return false;
    }
    array2=sqrr(array2);
    if (arrSame(array1, array2)) {
        return true
    }
    else return false;
}

function sqrr(array2) {
    var len = array2.length;
    for (var i=0;i<len;i++) {
        array2[i]=Math.sqrt(array2[i]);
    }
    return array2;
}

function arrSame(array1, array2) {
    if (array1.sort().join(',')=== array2.sort().join(',')) {
        return true;
    }
    else return false;
}
