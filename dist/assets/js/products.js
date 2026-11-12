/* Al-Bais Motors — parts catalogue.
   To add a part, copy one line and change it. Prices are not listed on
   purpose: stock and prices change, so customers ask on WhatsApp.
   icon: engine | brake | clutch | chain | electric | tyre | oil | accessory | filter | cable */
window.CATEGORIES = [
  { id: 'engine',     name: 'Engine Parts',          icon: 'engine' },
  { id: 'brakes',     name: 'Brakes',                icon: 'brake' },
  { id: 'clutch',     name: 'Clutch & Gearbox',      icon: 'clutch' },
  { id: 'chain',      name: 'Chain & Sprockets',     icon: 'chain' },
  { id: 'electrical', name: 'Electrical & Lights',   icon: 'electric' },
  { id: 'tyres',      name: 'Tyres & Tubes',         icon: 'tyre' },
  { id: 'oils',       name: 'Oils & Lubricants',     icon: 'oil' },
  { id: 'body',       name: 'Body & Accessories',    icon: 'accessory' }
];

window.BIKES = [
  'Honda CD 70', 'Honda CG 125', 'Honda Pridor', 'Honda CB 150F',
  'Yamaha YBR 125', 'Suzuki GD 110', 'Suzuki GS 150', 'Suzuki GR 150',
  '70cc (United, Road Prince, Unique & others)', '125cc (all local brands)'
];

window.PRODUCTS = [
  { id: 'piston-kit',      cat: 'engine',     icon: 'engine',    name: 'Piston & Ring Kit',          desc: 'Standard and oversize piston kits for a smooth, strong engine.',            fits: ['Honda CD 70', 'Honda CG 125', '70cc (United, Road Prince, Unique & others)', '125cc (all local brands)'] },
  { id: 'gasket-set',      cat: 'engine',     icon: 'engine',    name: 'Engine Gasket Set',          desc: 'Full and half gasket sets to stop oil leaks after engine work.',              fits: ['Honda CD 70', 'Honda CG 125', 'Yamaha YBR 125', 'Suzuki GS 150'] },
  { id: 'spark-plug',      cat: 'engine',     icon: 'electric',  name: 'Spark Plug',                 desc: 'Easy starting and better pickup. Ask for the right plug for your bike.',      fits: ['All bikes'] },
  { id: 'carburetor',      cat: 'engine',     icon: 'filter',    name: 'Carburetor',                 desc: 'Complete carburetors and repair kits for steady idle and mileage.',          fits: ['Honda CD 70', 'Honda CG 125', '70cc (United, Road Prince, Unique & others)'] },
  { id: 'air-filter',      cat: 'engine',     icon: 'filter',    name: 'Air Filter',                 desc: 'Keeps dust out of the engine — a cheap fix for poor pickup.',               fits: ['All bikes'] },
  { id: 'brake-shoes',     cat: 'brakes',     icon: 'brake',     name: 'Brake Shoes',                desc: 'Front and rear drum brake shoes for safe, even stopping.',                  fits: ['Honda CD 70', 'Honda CG 125', 'Suzuki GD 110', '70cc (United, Road Prince, Unique & others)'] },
  { id: 'disc-pads',       cat: 'brakes',     icon: 'brake',     name: 'Disc Brake Pads',            desc: 'Pads for bikes with a front disc brake.',                                   fits: ['Yamaha YBR 125', 'Suzuki GS 150', 'Suzuki GR 150', 'Honda CB 150F'] },
  { id: 'brake-cable',     cat: 'brakes',     icon: 'cable',     name: 'Brake & Clutch Cables',      desc: 'Smooth cables for brakes, clutch, throttle and speedometer.',               fits: ['All bikes'] },
  { id: 'clutch-plates',   cat: 'clutch',     icon: 'clutch',    name: 'Clutch Plates',              desc: 'Stops clutch slip so the bike pulls properly again.',                       fits: ['Honda CD 70', 'Honda CG 125', 'Yamaha YBR 125', 'Suzuki GS 150'] },
  { id: 'clutch-assembly', cat: 'clutch',     icon: 'clutch',    name: 'Clutch Assembly',            desc: 'Complete clutch assembly for heavy-use bikes.',                             fits: ['Honda CG 125', '125cc (all local brands)'] },
  { id: 'gear-lever',      cat: 'clutch',     icon: 'accessory', name: 'Gear Lever & Kick Lever',    desc: 'Replacement gear and kick-start levers.',                                   fits: ['Honda CD 70', 'Honda CG 125', '70cc (United, Road Prince, Unique & others)'] },
  { id: 'chain-kit',       cat: 'chain',      icon: 'chain',     name: 'Chain & Sprocket Kit',       desc: 'Matched chain, front and rear sprockets for a quiet, smooth ride.',         fits: ['Honda CD 70', 'Honda CG 125', 'Suzuki GD 110', 'Yamaha YBR 125'] },
  { id: 'chain-cover',     cat: 'chain',      icon: 'chain',     name: 'Chain Cover',                desc: 'Protects the chain and your clothes from grease.',                          fits: ['Honda CD 70', 'Honda CG 125'] },
  { id: 'battery',         cat: 'electrical', icon: 'electric',  name: 'Battery',                    desc: 'Batteries for kick and self-start bikes.',                                  fits: ['All bikes'] },
  { id: 'headlight',       cat: 'electrical', icon: 'electric',  name: 'Headlight & Bulbs',          desc: 'Headlight units, LED and standard bulbs for clear night riding.',           fits: ['All bikes'] },
  { id: 'indicators',      cat: 'electrical', icon: 'electric',  name: 'Indicators & Tail Light',    desc: 'Turn indicators, tail lights and backlight assemblies.',                    fits: ['All bikes'] },
  { id: 'cdi-coil',        cat: 'electrical', icon: 'electric',  name: 'CDI Unit & Ignition Coil',   desc: 'Fixes no-start and weak spark problems.',                                   fits: ['Honda CD 70', 'Honda CG 125', '70cc (United, Road Prince, Unique & others)'] },
  { id: 'tyre',            cat: 'tyres',      icon: 'tyre',      name: 'Motorcycle Tyres',           desc: 'Front and rear tyres in common sizes.',                                     fits: ['All bikes'] },
  { id: 'tube',            cat: 'tyres',      icon: 'tyre',      name: 'Tubes',                      desc: 'Strong inner tubes for front and rear wheels.',                             fits: ['All bikes'] },
  { id: 'engine-oil',      cat: 'oils',       icon: 'oil',       name: 'Engine Oil',                 desc: 'Quality 4-stroke engine oils. Ask which grade suits your bike.',            fits: ['All bikes'] },
  { id: 'chain-lube',      cat: 'oils',       icon: 'oil',       name: 'Chain Lube & Grease',        desc: 'Keeps the chain quiet and stops early wear.',                               fits: ['All bikes'] },
  { id: 'mirrors',         cat: 'body',       icon: 'accessory', name: 'Side Mirrors',               desc: 'Pairs of side mirrors in standard and sport styles.',                       fits: ['All bikes'] },
  { id: 'seat-cover',      cat: 'body',       icon: 'accessory', name: 'Seat Cover',                 desc: 'Comfortable, weather-proof seat covers.',                                   fits: ['All bikes'] },
  { id: 'mudguard',        cat: 'body',       icon: 'accessory', name: 'Mudguards & Side Covers',    desc: 'Front and rear mudguards and side panels.',                                 fits: ['Honda CD 70', 'Honda CG 125', '70cc (United, Road Prince, Unique & others)'] }
];
