public class Repro
{
	public static void main(String[] args) throws Exception
	{
		Thing t = new Thing("foo");
		t.AddJsonString("bar", "baz");
	}
}