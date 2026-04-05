'use client';
import { useState, useEffect } from 'react';
import { supabase } from '@/lib/supabase';

export default function Favorites() {
  const [items, setItems] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const getSaved = async () => {
      const { data } = await supabase
        .from('saved_dupes')
        .select('*')
        .order('created_at', { ascending: false });
      setItems(data || []);
      setLoading(false);
    };
    getSaved();
  }, []);

  const remove = async (id: number) => {
    await supabase.from('saved_dupes').delete().eq('id', id);
    setItems(items.filter(i => i.id !== id));
  };

  return (
    <main className="min-h-screen bg-black text-white p-8">
      <div className="max-w-5xl mx-auto">
        <header className="mb-16">
          <h1 className="text-3xl text-[#C9A96E] font-serif tracking-widest uppercase">My Collection</h1>
          <div className="h-px bg-zinc-900 w-full mt-4"></div>
        </header>

        {loading ? (
          <p className="text-center text-[#C9A96E] animate-pulse">Syncing with database...</p>
        ) : items.length === 0 ? (
          <p className="text-center opacity-20 tracking-widest uppercase text-xs py-20">Your wishlist is empty</p>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            {items.map((item) => (
              <div key={item.id} className="p-4 border border-zinc-900 bg-zinc-950/40 rounded-xl flex gap-6 items-center group relative">
                <button onClick={() => remove(item.id)} className="absolute top-2 right-2 opacity-0 group-hover:opacity-100 text-red-900 text-xs transition-all">REMOVE</button>
                <div className="w-24 h-24 bg-white rounded p-1 flex-shrink-0">
                  <img src={item.image} className="w-full h-full object-contain" alt="" />
                </div>
                <div className="flex-1">
                  <h3 className="text-[11px] font-medium leading-relaxed">{item.name}</h3>
                  <p className="text-xl text-[#C9A96E] mt-1">{item.price}</p>
                  <a href={item.link} target="_blank" className="text-[8px] uppercase tracking-widest text-zinc-500 hover:text-white mt-4 inline-block">Purchase Now →</a>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </main>
  );
}