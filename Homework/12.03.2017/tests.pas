unit tests;

interface

uses PUnit;

procedure task1(f: arrayOf<integer> -> arrayOf<integer>);
procedure task2(f: arrayOf<integer> -> integer);
procedure task3(f: arrayOf<integer> -> boolean);
procedure task4(input: arrayOf<integer>);
procedure task5(f: arrayOf<integer> -> integer);
procedure task6(f: arrayOf<integer> -> integer);
procedure task7(f: arrayOf<integer> -> integer);

procedure say(num: integer; count: integer);


implementation


var task4Dict := new SortedDictionary<integer, integer>();

procedure say(num: integer; count: integer);
begin
  if (task4Dict.ContainsKey(num)) then
    raise new Exception('Для одного числа можно только один раз вызвать say');
  
  task4Dict.Add(num, count);
end;

procedure task1(f: arrayOf<integer> -> arrayOf<integer>);
begin
  var run: seqOf<integer> -> seqOf<integer> := x -> f(x.ToArray).Sorted;
  
  assertSeqEq(run(seq(1, 2, 3, 4, 5)), seq(1, 2, 3, 4 ,5), 'test1');
  assertSeqEq(run(seq(1, 1, 1, 1, 1)), seq(1), 'test2');
  assertSeqEq(run(seq(1, 2, 1, 2, 1)), seq(1, 2), 'test3');
  assertSeqEq(run(seq(1, 2, 2, 3, 3, 3)), seq(1, 2, 3), 'test4');
  assertSeqEq(run(seq(3, 0, 0, 1, 0, 0, 3)), seq(0, 1, 3), 'test5');
  
  writeln('All tests are passed!');
end;

procedure task2(f: arrayOf<integer> -> integer);
begin
end;

procedure task3(f: arrayOf<integer> -> boolean);
begin
end;

procedure task4(input: arrayOf<integer>);
begin
  var d := new SortedDictionary<integer, integer>();
  
  foreach var x in input do
  begin
    if d.ContainsKey(x) then
      d[x] += 1
    else
      d[x] := 1;
  end;
  
  //assertSeqEq(d.ToArray, task4Dict.ToArray);
  writeln('Expected: ', d);
  writeln('Actual:   ', task4Dict);
  //writeln('All tests passed! Run again.');
end;

procedure task5(f: arrayOf<integer> -> integer);
begin
end;

procedure task6(f: arrayOf<integer> -> integer);
begin
end;

procedure task7(f: arrayOf<integer> -> integer);
begin
end;

begin
  
end.