unit PUnit;

interface

type
  arrayOf<T> = array of T;

procedure assertEq<T>(arg1: T; arg2: T; msg: string := '');

implementation

procedure assertEq<T>(arg1: T; arg2: T; msg: string);
begin
  if (arg1 <> arg2) then
  begin
    writeln('Assertion failed!', msg);
    writeln('Expected: ', arg1);
    writeln('Actual:   ', arg2);
  end;
end;


begin

end.