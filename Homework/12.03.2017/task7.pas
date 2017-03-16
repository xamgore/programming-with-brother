uses tests;

{ Дан массив целых чисел.
  Определить количество инверсий в массиве
    (т.е. таких пар элементов, в которых большее
    число находится слева от меньшего). }
  

function countInversions(a: array of integer): integer;
begin
  // ...
  result := 0;
end;


begin
  var arr: array of integer := (7, -4, 0, 0, -5, 7, 0, -7);
  writeln(countInversions(arr)); // 4

  // task7(countInversions);
end.