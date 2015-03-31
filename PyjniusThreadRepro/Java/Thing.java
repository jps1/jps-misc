// package PyjniusThreadRepro.Things;

import java.util.Map;
import java.util.LinkedHashMap;

public class Thing {

	public Thing(String name)
	{
		this.jsonstrings = new LinkedHashMap<String, String>();
		this.name = name;
	}

	public void AddJsonString(String key, String jsonstr)
	{
		System.out.println("(Java) Adding json-string \"" + key + "\" to thing \"" + name + "\"");
		jsonstrings.put(key, jsonstr);
	}

	private String name;
	public String getName() { return name; }

	private Map<String, String> jsonstrings;

	public int GetNumOfJsonStrings() { return jsonstrings.size(); }
}