function findMins(arr: array of integer): (integer, integer);
begin
  var min1 := arr[0];
  var min2 := arr[1];
  
  if (min1 > min2) then
    Swap(min1, min2);
  
  for var i := 2 to arr.Length - 1 do
  begin
    if min1 >= arr[i] then
    begin
      swap(min1, min2);
      min1 := arr[i];
    end;
    if (min2 >= arr[i]) and (arr[i] <> min1) then
      min2 := arr[i];
  end;
  
  result := (min1, min2);
end;


begin
  //var S := 100;
  //  var arr := arrrandom(s, 0, 5);
  //var arr: array of integer := (0, 0, 3, 5, 5, 5);
  //writeln(arr);
  
  
  
  var t1: array of integer := (0, 1, 2, 3);
  (var tm1, var tm2) := findMins(t1);
  assert((tm1 = 0) and (tm2 = 1), 'test1');
  
  var t2: array of integer := (1, 1, 2, 3);
  (var t2m1, var t2m2) := findMins(t2);
  assert((t2m1 = 1) and (t2m2 = 1), 'test2');
  
  var t3: array of integer := (3, 1, 2, 1);
  (var t3m1, var t3m2) := findMins(t3);
  assert((t3m1 = 1) and (t3m2 = 1), 'test3');
  
  var t4: array of integer := (1, 0, 2, 3);
  (var t4m1, var t4m2) := findMins(t4);
  assert((t4m1 = 0) and (t4m2 = 1), 'test4');
  
  var t5: array of integer := (2, 3, 0, 1);
  (var t5m1, var t5m2) := findMins(t5);
  assert((t5m1 = 0) and (t5m2 = 1), 'test5');
end.