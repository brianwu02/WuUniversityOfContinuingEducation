defmodule InfiniteNumbers do
  @moduledoc """
  Returns a stream of numbers starting from start

  iex> InfiniteNumbers.from(0) |> Stream.map(&IO.inspect/1) |> Enum.to_list
  iex> InfiniteNumbers.from(50) |> Stream.each(IO.inspect/1) |> Stream.run
  """
  def from(start) do
    Stream.resource(
      fn -> start end,
      fn(num) ->
        {[num + 1], num + 1}
      end,
      fn(num) -> num end
    )
  end
end

defmodule FizzBuzzer do
  @moduledoc """
  A standard fizzbuzz implementation using pattern matching

  iex> 1..10 |> Enum.each(&FizzBuzzer.fizz_buzz/1)
  """
  def fizz_buzz(n) when rem(n, 3) == 0 and rem(n, 5), do: "fizzbuzz"
  def fizz_buzz(n) when rem(n, 3) == 0, do: "fizz"
  def fizz_buzz(n) when rem(n, 5) == 0, do: "buzz"
  def fizz_buzz(n), do: n
end

defmodule RunFizz do
  @moduledoc """
  different variations of fizzbuzz using Enum and Streams
  """
  def fizzbuzz_1 do
    fizzbuzz_1 =
      InfiniteNumbers.from(0)
      |> Stream.map(&FizzBuzzer.fizz_buzz/1)
      |> Enum.each(&IO.puts/1)
  end

  def fizzbuzz_2 do
    fizz_buzz_2 = 
      InfiniteNumbers.from(0) 
      |> Stream.each(&IO.inspect/1)
      |> Stream.run
  end

  def fizzbuzz_3 do
    fizz_buzz_3 =
      InfiniteNumbers.from(0)
      |> Enum.take(10) # this will generate a list prior
      |> Enum.map(&FizzBuzzer.fizz_buzz/1)
  end

  def fizzbuzz_4 do
    1..10 |> Enum.map(&FizzBuzzer.fizz_buzz/1) |> IO.inspect
  end

end
