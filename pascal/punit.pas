unit PUnit;

interface

type
  arrayOf<T> = array of T;
  seqOf<T> = sequence of T;

procedure assertEq<T>(arg1: T; arg2: T; msg: string := '');

procedure assertSeqEq<T>(arg1: sequence of T; arg2: sequence of T; msg: string := '');

implementation

function Sorted<T>(self: array of T): array of T; extensionmethod;
begin
  var p := self.ToArray();
  System.Array.Sort(p);
  result := p;
end;

function Sorted<T>(self: sequence of T): sequence of T; extensionmethod;
begin
  var p := self.ToArray();
  System.Array.Sort(p);
  result := p;
end;

procedure assertEq<T>(arg1: T; arg2: T; msg: string);
begin
  if (arg1 <> arg2) then
  begin
    writeln('Assertion failed! ', msg);
    writeln('Expected: ', arg1);
    writeln('Actual:   ', arg2, NewLine);
    halt();
  end;
end;

procedure assertSeqEq<T>(arg1: sequence of T; arg2: sequence of T; msg: string);
begin
  var arr2 := arg2.ToArray;
  var arr1 := arg1.ToArray;

  if not arr1.SequenceEqual(arr2) then
  begin
//    writeln('Assertion failed! ', msg);
//    writeln('Expected:   ', string.Join(', ', arr1));
//    write('Actual:     ');
    
    (var x, var y) := 
      arr1.Zip(arr2, (x, y) -> (x, y))
          .Where(pair -> pair[0] <> pair[1])
          .First();
    
    writeln('Difference: ', x, ' ', y, NewLine);
    halt();
  end;
end;

begin

end.