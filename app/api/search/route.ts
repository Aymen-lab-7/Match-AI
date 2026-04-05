import { NextResponse } from 'next/server';

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const query = searchParams.get('q');
  const apiKey = "72c5f0b38aef7f3819c6c3f678b233631ba327a065df23e39cf2efdd199426f5";

  if (!query) return NextResponse.json({ error: 'Missing query' }, { status: 400 });

  try {
    const url = `https://serpapi.com/search.json?engine=google_shopping&q=${encodeURIComponent(query)}&api_key=${apiKey}`;
    const response = await fetch(url);
    const data = await response.json();
    
    return NextResponse.json(data);
  } catch (error) {
    return NextResponse.json({ error: 'Failed to fetch data' }, { status: 500 });
  }
}