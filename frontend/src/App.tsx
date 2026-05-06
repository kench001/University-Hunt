import { useState, useEffect } from 'react'
import universityData from './data/metro_manila_universities.json'
import { Search, GitCompare as CompareIcon, Filter, MapPin, GraduationCap, DollarSign, BookOpen, ChevronLeft, Globe, Award, Info, List, Clock, Map as MapIcon, ArrowUpRight } from 'lucide-react'
import { motion, AnimatePresence } from 'framer-motion'
import SplashScreen from './components/SplashScreen'

// Types
type University = {
  name: string
  type: string
  website: string
  info: string
  ph_ranking: string
  qs_asia_rank_2026: string | number
  acceptance_rate: string
  total_estimated_students: string
  programs: string[]
  tuition: Record<string, string>
  city?: string
}

export default function App() {
  const [searchTerm, setSearchTerm] = useState('')
  const [selectedCity, setSelectedCity] = useState<string>('All')
  const [selectedType, setSelectedType] = useState<string>('All')
  const [compareList, setCompareList] = useState<University[]>([])
  const [isComparing, setIsComparing] = useState(false)
  const [selectedUni, setSelectedUni] = useState<University | null>(null)
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    const timer = setTimeout(() => {
      setIsLoading(false)
    }, 2500)
    return () => clearTimeout(timer)
  }, [])

  const allUniversities = universityData.cities.flatMap(city => 
    city.universities.map(u => ({ ...u, city: city.name }))
  )

  const filteredUniversities = allUniversities.filter(u => {
    const matchesSearch = u.name.toLowerCase().includes(searchTerm.toLowerCase()) || 
                         u.programs.some(p => p.toLowerCase().includes(searchTerm.toLowerCase()))
    const matchesCity = selectedCity === 'All' || u.city === selectedCity
    const matchesType = selectedType === 'All' || u.type === selectedType
    return matchesSearch && matchesCity && matchesType
  })

  const cities = ['All', ...universityData.cities.map(c => c.name)]

  const toggleCompare = (e: React.MouseEvent, uni: University) => {
    e.stopPropagation()
    if (compareList.some(u => u.name === uni.name)) {
      setCompareList(compareList.filter(u => u.name !== uni.name))
    } else if (compareList.length < 2) {
      setCompareList([...compareList, uni])
    }
  }

  return (
    <div className="min-h-screen font-sans bg-sky-mist">
      <AnimatePresence mode="wait">
        {isLoading ? (
          <SplashScreen key="splash" />
        ) : (
          <motion.div
            key="content"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.8 }}
          >
            {/* NAVIGATION */}
            <nav className="fixed top-0 left-0 w-full z-50 bg-white/70 backdrop-blur-md border-b border-black/5 px-8 py-4">
              <div className="max-w-7xl mx-auto flex justify-between items-center">
                <div className="flex items-center gap-2 cursor-pointer" onClick={() => setSelectedUni(null)}>
                  <div className="w-8 h-8 bg-midnight rounded-lg flex items-center justify-center text-white">
                    <GraduationCap size={20} />
                  </div>
                  <span className="text-xl font-display font-bold tracking-tight">University Hunt</span>
                </div>
                
                <div className="hidden md:flex items-center gap-8 text-sm font-medium text-midnight/60">
                  {['Universities', 'Programs', 'Admissions', 'Resources'].map(item => (
                    <a key={item} href="#" className="hover:text-sunset-orange transition-colors">{item}</a>
                  ))}
                </div>

                <div className="flex items-center gap-4">
                  <button className="text-sm font-medium hover:text-sunset-orange transition-colors">Login</button>
                  <button className="bg-midnight text-white px-6 py-2 rounded-full text-sm font-bold flex items-center gap-2 group hover:bg-midnight/90 transition-all">
                    Start your hunt
                    <div className="bg-sunset-orange w-5 h-5 rounded flex items-center justify-center transition-transform group-hover:translate-x-1 group-hover:-translate-y-1">
                      <ArrowUpRight size={14} className="text-white" />
                    </div>
                  </button>
                </div>
              </div>
            </nav>

            <AnimatePresence mode="wait">
              {!selectedUni ? (
                <motion.div
                  key="listing"
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  exit={{ opacity: 0 }}
                  className="pt-20"
                >
                  {/* HERO SECTION */}
                  <header className="sky-bg pt-24 pb-32 px-8 text-center relative overflow-hidden">
                    <div className="max-w-4xl mx-auto relative z-10">
                      <motion.div
                        initial={{ y: 30, opacity: 0 }}
                        animate={{ y: 0, opacity: 1 }}
                        transition={{ duration: 1, ease: [0.22, 1, 0.36, 1] }}
                      >
                        <div className="inline-flex items-center gap-2 bg-white/50 backdrop-blur-sm border border-black/5 px-4 py-1.5 rounded-full mb-8 shadow-sm">
                          <div className="w-2 h-2 rounded-full bg-sunset-orange animate-pulse" />
                          <span className="text-[10px] font-bold uppercase tracking-[0.2em] text-midnight/50">2026 Admissions Now Open</span>
                        </div>
                        
                        <h1 className="text-6xl md:text-8xl font-display mb-8 leading-[1.1] tracking-tight">
                          One portal for every <br />
                          <span className="text-sunset-orange">student & university</span>
                        </h1>
                        
                        <p className="text-lg md:text-xl text-muted-steel max-w-2xl mx-auto mb-12 leading-relaxed">
                          A modern guide to Metro Manila's top educational institutions. Search, compare, and plan your academic future with clarity and structured space.
                        </p>

                        <div className="flex flex-wrap justify-center gap-4 mb-20">
                          <button className="bg-midnight text-white px-8 py-4 rounded-full font-bold flex items-center gap-3 group shadow-xl hover:shadow-sunset-orange/20 transition-all">
                            Search Universities
                            <div className="bg-sunset-orange w-6 h-6 rounded flex items-center justify-center transition-transform group-hover:translate-x-1 group-hover:-translate-y-1">
                              <ArrowUpRight size={16} className="text-white" />
                            </div>
                          </button>
                          <button className="bg-white text-midnight px-8 py-4 rounded-full font-bold border border-black/10 hover:bg-sky-mist transition-all shadow-sm">
                            Compare Schools
                          </button>
                        </div>
                      </motion.div>

                      {/* LOGO CLOUD */}
                      <div className="pt-16 border-t border-black/5">
                        <p className="text-[10px] font-bold uppercase tracking-[0.3em] text-midnight/30 mb-10">Top Institutions Featured</p>
                        <div className="flex flex-wrap justify-center gap-12 md:gap-20 opacity-30 grayscale contrast-125">
                          {['UP', 'ADMU', 'DLSU', 'UST', 'FEU', 'PUP'].map(uni => (
                            <span key={uni} className="text-2xl font-display font-black tracking-widest">{uni}</span>
                          ))}
                        </div>
                      </div>
                    </div>
                  </header>

                  {/* SEARCH & FILTERS BAR */}
                  <div className="sticky top-[73px] z-40 px-8 py-4 bg-sky-mist/80 backdrop-blur-md border-b border-black/5">
                    <div className="max-w-7xl mx-auto flex flex-col md:flex-row gap-4 items-center">
                      <div className="relative flex-grow w-full">
                        <Search className="absolute left-6 top-1/2 -translate-y-1/2 text-midnight/30" size={20} />
                        <input 
                          type="text" 
                          placeholder="Search schools, programs, or cities..." 
                          className="w-full soft-input pl-14 py-3 text-lg"
                          value={searchTerm}
                          onChange={(e) => setSearchTerm(e.target.value)}
                        />
                      </div>
                      <div className="flex gap-4 w-full md:w-auto">
                        <select 
                          className="flex-grow md:w-48 soft-input py-3 text-sm font-medium"
                          value={selectedCity}
                          onChange={(e) => setSelectedCity(e.target.value)}
                        >
                          {cities.map(city => <option key={city} value={city}>{city}</option>)}
                        </select>
                        <button 
                          onClick={() => setIsComparing(!isComparing)}
                          className={`soft-button py-3 text-sm ${compareList.length === 2 ? 'bg-sunset-orange text-white' : 'bg-midnight text-white'}`}
                        >
                          <CompareIcon size={16} />
                          {isComparing ? 'Close Compare' : `Compare (${compareList.length}/2)`}
                        </button>
                      </div>
                    </div>
                  </div>

                  <main className="max-w-7xl mx-auto px-8 py-16">
                    <AnimatePresence mode="wait">
                      {isComparing && compareList.length === 2 ? (
                        <motion.div 
                          key="comparison"
                          initial={{ opacity: 0, y: 20 }}
                          animate={{ opacity: 1, y: 0 }}
                          exit={{ opacity: 0, y: -20 }}
                          className="grid grid-cols-1 md:grid-cols-2 gap-8"
                        >
                          {compareList.map(uni => (
                            <UniversityCard 
                              key={uni.name} 
                              uni={uni} 
                              onCompare={toggleCompare} 
                              compareList={compareList}
                              onClick={() => setSelectedUni(uni)}
                            />
                          ))}
                        </motion.div>
                      ) : (
                        <motion.div 
                          key="list"
                          initial={{ opacity: 0 }}
                          animate={{ opacity: 1 }}
                          className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"
                        >
                          {filteredUniversities.length > 0 ? (
                            filteredUniversities.map((uni, idx) => (
                              <motion.div 
                                key={uni.name}
                                initial={{ opacity: 0, y: 20 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: idx * 0.05 }}
                              >
                                <UniversityCard 
                                  uni={uni} 
                                  onCompare={toggleCompare} 
                                  compareList={compareList}
                                  onClick={() => setSelectedUni(uni)}
                                />
                              </motion.div>
                            ))
                          ) : (
                            <div className="col-span-full py-32 text-center">
                              <GraduationCap size={64} className="mx-auto mb-6 text-midnight/5" />
                              <h2 className="text-4xl mb-4">No schools matched your hunt.</h2>
                              <p className="text-muted-steel font-bold uppercase tracking-widest text-sm">Try adjusting your search criteria</p>
                            </div>
                          )}
                        </motion.div>
                      )}
                    </AnimatePresence>
                  </main>
                </motion.div>
              ) : (
                /* UNIVERSITY DETAIL VIEW */
                <motion.div
                  key="detail"
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  exit={{ opacity: 0 }}
                  className="min-h-screen bg-white pt-20"
                >
                  <div className="max-w-7xl mx-auto px-8 py-12">
                    <button 
                      onClick={() => setSelectedUni(null)}
                      className="flex items-center gap-2 text-muted-steel hover:text-midnight mb-12 transition-colors font-bold uppercase text-xs tracking-widest"
                    >
                      <ChevronLeft size={16} /> Back to Search
                    </button>

                    <div className="flex flex-col lg:flex-row gap-16 items-start">
                      {/* Hero Info */}
                      <div className="flex-grow">
                        <div className="inline-flex gap-2 mb-6">
                          <span className="soft-tag bg-sunset-orange/10 text-sunset-orange">{selectedUni.type}</span>
                          <span className="soft-tag bg-midnight/5 text-midnight/40">{selectedUni.city}</span>
                        </div>
                        <h1 className="text-5xl md:text-7xl mb-8">{selectedUni.name}</h1>
                        <p className="text-xl text-muted-steel leading-relaxed mb-12 max-w-3xl">
                          {selectedUni.info} {selectedUni.name} stands as a beacon of academic excellence in the heart of {selectedUni.city}, offering world-class programs and fostering a community of innovators.
                        </p>

                        <div className="grid grid-cols-2 md:grid-cols-4 gap-8 mb-16">
                          <div>
                            <p className="text-[10px] font-bold text-midnight/30 uppercase tracking-[0.2em] mb-2">Location</p>
                            <p className="font-bold flex items-center gap-1"><MapPin size={14} /> {selectedUni.city}</p>
                          </div>
                          <div>
                            <p className="text-[10px] font-bold text-midnight/30 uppercase tracking-[0.2em] mb-2">Website</p>
                            <p className="font-bold flex items-center gap-1 overflow-hidden text-ellipsis whitespace-nowrap">
                              <Globe size={14} className="flex-shrink-0" /> 
                              <a href={selectedUni.website} target="_blank" rel="noopener noreferrer" className="hover:text-sunset-orange transition-colors">
                                {selectedUni.website.replace('https://', '').replace('www.', '')}
                              </a>
                            </p>
                          </div>
                          <div>
                            <p className="text-[10px] font-bold text-midnight/30 uppercase tracking-[0.2em] mb-2">Type</p>
                            <p className="font-bold flex items-center gap-1"><Award size={14} /> {selectedUni.type}</p>
                          </div>
                          <div>
                            <p className="text-[10px] font-bold text-midnight/30 uppercase tracking-[0.2em] mb-2">QS Asia Rank</p>
                            <p className="font-bold flex items-center gap-1 text-sunset-orange"><Award size={14} /> {selectedUni.qs_asia_rank_2026}</p>
                          </div>
                        </div>

                        <div className="space-y-12">
                          <section>
                            <h3 className="text-2xl font-bold mb-6 flex items-center gap-2">
                              <DollarSign size={24} className="text-sunset-orange" /> Tuition Fees
                            </h3>
                            <div className="grid grid-cols-1 gap-4">
                              {Object.entries(selectedUni.tuition).map(([key, value]) => (
                                <div key={key} className="p-6 bg-sky-mist rounded-2xl border border-black/5 flex flex-col md:flex-row md:justify-between md:items-center gap-2">
                                  <span className="font-bold uppercase text-[10px] tracking-[0.1em] text-midnight/40">{key.replace(/_/g, ' ')}</span>
                                  <span className="font-medium text-midnight">{value}</span>
                                </div>
                              ))}
                            </div>
                          </section>
                          <section>
                            <h3 className="text-2xl font-bold mb-6 flex items-center gap-2">
                              <BookOpen size={24} className="text-sunset-orange" /> Featured Programs
                            </h3>
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                              {selectedUni.programs.map(p => (
                                <div key={p} className="p-4 bg-sky-mist rounded-xl border border-black/5 font-medium flex justify-between items-center group cursor-default hover:bg-white hover:shadow-premium transition-all">
                                  {p}
                                  <ArrowUpRight size={14} className="opacity-0 group-hover:opacity-30 transition-opacity" />
                                </div>
                              ))}
                            </div>
                          </section>

                          <section>
                            <h3 className="text-2xl font-bold mb-6 flex items-center gap-2">
                              <Clock size={24} className="text-sunset-orange" /> Admissions
                            </h3>
                            <div className="p-8 bg-midnight text-white rounded-3xl">
                              <p className="text-white/60 mb-4">The main application period typically opens from October to January. Early bird discounts and scholarship applications are encouraged.</p>
                              <button className="text-sunset-orange font-bold flex items-center gap-2 group">
                                View Admission Requirements <ArrowUpRight size={16} className="transition-transform group-hover:translate-x-1 group-hover:-translate-y-1" />
                              </button>
                            </div>
                          </section>
                        </div>
                      </div>

                      {/* Sidebar */}
                      <div className="w-full lg:w-96 space-y-8">
                        <div className="bg-white p-8 rounded-3xl border border-black/5 shadow-premium sticky top-32">
                          <h4 className="text-sm font-bold uppercase tracking-widest text-midnight/30 mb-8">Summary</h4>
                          <div className="space-y-6">
                            <div className="flex justify-between items-center pb-4 border-b border-black/5">
                              <span className="text-sm text-muted-steel font-medium">PH Ranking</span>
                              <span className="font-bold text-right text-xs max-w-[180px]">{selectedUni.ph_ranking}</span>
                            </div>
                            <div className="flex justify-between items-center pb-4 border-b border-black/5">
                              <span className="text-sm text-muted-steel font-medium">Acceptance Rate</span>
                              <span className="font-bold">{selectedUni.acceptance_rate}</span>
                            </div>
                            <div className="flex justify-between items-center pb-4 border-b border-black/5">
                              <span className="text-sm text-muted-steel font-medium">Total Students</span>
                              <span className="font-bold">{selectedUni.total_estimated_students}</span>
                            </div>
                          </div>
                          <button className="w-full bg-sunset-orange text-white py-4 rounded-full font-bold mt-10 shadow-lg shadow-sunset-orange/20 hover:scale-[1.02] transition-all">
                            Add to Comparison
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                </motion.div>
              )}
            </AnimatePresence>

            {/* FOOTER */}
            <footer className="bg-midnight text-white py-24 px-8 mt-20">
              <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-12 mb-20">
                <div className="md:col-span-2">
                  <div className="flex items-center gap-2 mb-6">
                    <div className="w-8 h-8 bg-white rounded-lg flex items-center justify-center text-midnight">
                      <GraduationCap size={20} />
                    </div>
                    <span className="text-2xl font-display font-bold tracking-tight">University Hunt</span>
                  </div>
                  <p className="text-white/40 max-w-sm mb-8 leading-relaxed">
                    Empowering the next generation of students with the data they need to make informed decisions about their academic future in Metro Manila.
                  </p>
                </div>
                <div>
                  <h5 className="font-bold mb-6 text-sm uppercase tracking-widest text-sunset-orange">Resources</h5>
                  <ul className="space-y-4 text-white/60 text-sm font-medium">
                    <li><a href="#" className="hover:text-white transition-colors">University List</a></li>
                    <li><a href="#" className="hover:text-white transition-colors">Program Guide</a></li>
                    <li><a href="#" className="hover:text-white transition-colors">Scholarship Hub</a></li>
                    <li><a href="#" className="hover:text-white transition-colors">FAQ</a></li>
                  </ul>
                </div>
                <div>
                  <h5 className="font-bold mb-6 text-sm uppercase tracking-widest text-sunset-orange">Company</h5>
                  <ul className="space-y-4 text-white/60 text-sm font-medium">
                    <li><a href="#" className="hover:text-white transition-colors">About Us</a></li>
                    <li><a href="#" className="hover:text-white transition-colors">Contact</a></li>
                    <li><a href="#" className="hover:text-white transition-colors">Privacy Policy</a></li>
                    <li><a href="#" className="hover:text-white transition-colors">Terms of Service</a></li>
                  </ul>
                </div>
              </div>
              <div className="max-w-7xl mx-auto pt-12 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-8">
                <p className="text-white/20 text-xs font-bold uppercase tracking-[0.2em]">© 2026 Metro Manila Education Guide. All rights reserved.</p>
                <div className="flex gap-8 opacity-40 hover:opacity-100 transition-opacity">
                  {['Instagram', 'Twitter', 'LinkedIn'].map(social => (
                    <a key={social} href="#" className="text-xs font-bold uppercase tracking-widest hover:text-sunset-orange transition-colors">{social}</a>
                  ))}
                </div>
              </div>
            </footer>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  )
}

function UniversityCard({ uni, onCompare, compareList, onClick }: { uni: University, onCompare: (e: React.MouseEvent, u: University) => void, compareList: University[], onClick: () => void }) {
  const isCompared = compareList.some(u => u.name === uni.name)
  
  return (
    <div 
      onClick={onClick}
      className="soft-card group cursor-pointer relative overflow-hidden flex flex-col h-full"
    >
      <div className="flex justify-between items-start mb-6">
        <div className="flex gap-2">
          <span className={`soft-tag ${uni.type === 'Public' ? 'bg-sunset-orange/10 text-sunset-orange border-sunset-orange/10' : 'bg-midnight/5 text-midnight/40 border-midnight/5'}`}>
            {uni.type}
          </span>
          <span className="soft-tag bg-sky-mist text-muted-steel/60 italic">
            {uni.city}
          </span>
        </div>
        <button 
          onClick={(e) => onCompare(e, uni)}
          className={`w-10 h-10 rounded-full border border-black/10 flex items-center justify-center transition-all ${isCompared ? 'bg-sunset-orange text-white border-sunset-orange shadow-lg' : 'bg-white hover:border-sunset-orange hover:text-sunset-orange'}`}
          title="Compare"
        >
          <CompareIcon size={16} />
        </button>
      </div>
      
      <h2 className="text-2xl mb-4 leading-tight font-display font-bold group-hover:text-sunset-orange transition-colors">{uni.name}</h2>
      <p className="text-sm text-muted-steel mb-8 line-clamp-2 leading-relaxed flex-grow">
        {uni.info}
      </p>
      
      <div className="flex flex-wrap gap-2 mb-8">
        {uni.programs.slice(0, 3).map(p => (
          <span key={p} className="text-[10px] font-bold text-midnight/40 bg-sky-mist px-2.5 py-1 rounded-md uppercase tracking-widest">{p}</span>
        ))}
        {uni.programs.length > 3 && <span className="text-[10px] font-bold text-sunset-orange">+{uni.programs.length - 3}</span>}
      </div>
      
      <div className="pt-6 border-t border-black/5 flex justify-between items-center mt-auto">
        <div className="flex flex-col">
          <span className="text-[9px] font-bold text-midnight/30 uppercase tracking-[0.2em]">Est. Tuition</span>
          <span className="font-display text-lg font-bold">
            {Object.values(uni.tuition)[0].includes('Free') ? 'Free Tuition' : Object.values(uni.tuition)[0].split(' ')[1] || Object.values(uni.tuition)[0].split(' ')[0]}
          </span>
        </div>
        <div className="text-sunset-orange opacity-0 group-hover:opacity-100 transition-all flex items-center gap-1 font-bold text-[10px] uppercase tracking-widest">
          Details <ArrowUpRight size={12} />
        </div>
      </div>
    </div>
  )
}
