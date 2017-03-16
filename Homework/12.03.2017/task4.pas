uses tests;

{ Дан массив целых чисел.
  Для каждого из чисел, входящего в массив, вывести,
    сколько раз оно входит в массив. }
  

procedure countElems(a: array of integer);
begin
  // ...
  
  say(7, 3);  // семёрка входит три раза
  say(4, 1);
  say(5, 1);
  say(0, 2);
end;


begin
  // var arr := ArrRandom(20, 0, 5);
  var arr: array of integer := (7, 4, 0, 5, 7, 0, 7);
  
  countElems(arr);
  task4(arr);  // run program several times
end.