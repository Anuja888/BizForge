// ===== INTERNATIONALIZATION (i18n) =====

const translations = {
    en: {
        // Hero
        hero_title: "AI-Powered Brand Generation",
        hero_subtitle: "Create stunning brands, logos, and marketing content in seconds with advanced AI",
        cta_primary: "Launch Studio",
        cta_secondary: "Learn More",
        
        // Features
        feature_ai: "🤖 AI-Powered",
        feature_fast: "⚡ Lightning Fast",
        feature_multilingual: "🌍 Multilingual",
        features_title: "Powerful Features",
        features_subtitle: "Everything you need to build your brand",
        feature_brand_title: "Brand Names",
        feature_brand_desc: "Generate creative, memorable names that resonate with your audience",
        feature_logo_title: "Logo Design",
        feature_logo_desc: "AI-generated professional logos using Stable Diffusion XL",
        feature_content_title: "Marketing Content",
        feature_content_desc: "Craft compelling taglines, headlines, and descriptions instantly",
        feature_color_title: "Color Palettes",
        feature_color_desc: "Get perfectly matched color schemes for your brand identity",
        feature_sentiment_title: "Sentiment Analysis",
        feature_sentiment_desc: "Understand the emotional tone of your marketing messages",
        feature_chat_title: "AI Consultant",
        feature_chat_desc: "Get expert brand strategy advice powered by advanced AI",
        
        // Why Section
        why_title: "Why Choose BizForge?",
        why_subtitle: "The smarter choice for brand creation",
        why_speed: "Lightning Speed",
        why_speed_desc: "Get results in seconds, not days",
        why_accuracy: "AI-Powered Accuracy",
        why_accuracy_desc: "Advanced algorithms trained on millions of brands",
        why_cost: "Affordable",
        why_cost_desc: "No expensive designer fees or agency costs",
        why_global: "Global Reach",
        why_global_desc: "Support for 5+ languages across all features",
        why_easy: "Easy to Use",
        why_easy_desc: "Intuitive interface, no design experience needed",
        why_iterate: "Unlimited Iterations",
        why_iterate_desc: "Generate variations until you find perfection",
        
        // Footer
        footer_tagline: "AI-Powered Brand Generation Platform",
        footer_resources: "Resources",
        footer_launch: "Launch Studio",
        footer_features: "Features",
        footer_docs: "Documentation",
        footer_legal: "Legal",
        footer_privacy: "Privacy Policy",
        footer_terms: "Terms of Service",
        footer_copyright: "© 2024 BizForge. All rights reserved.",
        
        // Studio
        studio_title: "Brand Studio",
        tab_brand: "Brand Names",
        tab_logo: "Logo Design",
        tab_content: "Marketing",
        tab_design: "Design System",
        tab_sentiment: "Sentiment",
        tab_chat: "AI Chat",
        
        // Brand Tab
        brand_title: "Generate Brand Names",
        brand_desc: "Get creative, memorable names for your business",
        
        // Logo Tab
        logo_title: "Generate Logo",
        logo_desc: "Create professional AI-generated logos for your brand",
        
        // Content Tab
        content_title: "Generate Marketing Content",
        content_desc: "Create compelling taglines and descriptions",
        
        // Design Tab
        design_title: "Design System",
        design_desc: "Generate color palettes and design guidelines",
        
        // Sentiment Tab
        sentiment_title: "Sentiment Analysis",
        sentiment_desc: "Analyze the emotional tone of your content",
        
        // Chat Tab
        chat_title: "AI Consultant",
        chat_desc: "Get expert advice on your brand strategy",
        chat_welcome: "Welcome to BizForge AI Consultant! Ask me anything about your brand strategy.",
        
        // Forms
        form_description: "Business Description",
        form_brand_name: "Brand Name",
        form_text: "Text to Analyze",
        form_style: "Design Style",
        style_modern: "Modern",
        style_classic: "Classic",
        style_playful: "Playful",
        style_minimal: "Minimal",
        
        // Buttons
        btn_generate: "Generate Names",
        btn_generate_logo: "Generate Logo",
        btn_generate_content: "Generate Content",
        btn_generate_design: "Generate Palette",
        btn_analyze: "Analyze",
        btn_send: "Send",
        btn_download: "Download",
        
        // Results
        tagline: "Tagline",
        headline: "Headline",
        description: "Description",
        score: "Score",
        explanation: "Analysis",
        
        // Loading
        loading: "Generating...",
        loading_logo: "Generating logo... This may take 20-30 seconds"
    },
    
    es: {
        hero_title: "Generación de Marcas Impulsada por IA",
        hero_subtitle: "Crea marcas, logotipos y contenido de marketing impresionantes en segundos con IA avanzada",
        cta_primary: "Lanzar Studio",
        cta_secondary: "Más información",
        
        feature_ai: "🤖 Impulsado por IA",
        feature_fast: "⚡ Ultra Rápido",
        feature_multilingual: "🌍 Multilingüe",
        features_title: "Características Potentes",
        features_subtitle: "Todo lo que necesitas para construir tu marca",
        feature_brand_title: "Nombres de Marca",
        feature_brand_desc: "Genera nombres creativos y memorables que resuenen con tu audiencia",
        feature_logo_title: "Diseño de Logo",
        feature_logo_desc: "Logotipos profesionales generados por IA usando Stable Diffusion XL",
        feature_content_title: "Contenido de Marketing",
        feature_content_desc: "Crea eslóganes, titulares y descripciones convincentes al instante",
        feature_color_title: "Paletas de Color",
        feature_color_desc: "Obtén esquemas de color perfectamente combinados para tu identidad de marca",
        feature_sentiment_title: "Análisis de Sentimiento",
        feature_sentiment_desc: "Comprende el tono emocional de tus mensajes de marketing",
        feature_chat_title: "Consultor de IA",
        feature_chat_desc: "Obtén consejos de estrategia de marca de expertos impulsados por IA avanzada",
        
        why_title: "¿Por Qué Elegir BizForge?",
        why_subtitle: "La opción inteligente para crear marcas",
        why_speed: "Ultra Rápido",
        why_speed_desc: "Obtén resultados en segundos, no en días",
        why_accuracy: "Precisión Impulsada por IA",
        why_accuracy_desc: "Algoritmos avanzados entrenados en millones de marcas",
        why_cost: "Asequible",
        why_cost_desc: "Sin honorarios costosos de diseñador ni costos de agencia",
        why_global: "Alcance Global",
        why_global_desc: "Soporte para 5+ idiomas en todas las características",
        why_easy: "Fácil de Usar",
        why_easy_desc: "Interfaz intuitiva, sin experiencia en diseño necesaria",
        why_iterate: "Iteraciones Ilimitadas",
        why_iterate_desc: "Genera variaciones hasta encontrar la perfección",
        
        footer_tagline: "Plataforma de Generación de Marcas Impulsada por IA",
        footer_resources: "Recursos",
        footer_launch: "Lanzar Studio",
        footer_features: "Características",
        footer_docs: "Documentación",
        footer_legal: "Legal",
        footer_privacy: "Política de Privacidad",
        footer_terms: "Términos de Servicio",
        footer_copyright: "© 2024 BizForge. Todos los derechos reservados.",
        
        studio_title: "Studio de Marca",
        tab_brand: "Nombres de Marca",
        tab_logo: "Diseño de Logo",
        tab_content: "Marketing",
        tab_design: "Sistema de Diseño",
        tab_sentiment: "Sentimiento",
        tab_chat: "Chat de IA",
        
        brand_title: "Generar Nombres de Marca",
        brand_desc: "Obtén nombres creativos y memorables para tu negocio",
        
        logo_title: "Generar Logo",
        logo_desc: "Crea logotipos profesionales generados por IA para tu marca",
        
        content_title: "Generar Contenido de Marketing",
        content_desc: "Crea eslóganes y descripciones convincentes",
        
        design_title: "Sistema de Diseño",
        design_desc: "Genera paletas de color y directrices de diseño",
        
        sentiment_title: "Análisis de Sentimiento",
        sentiment_desc: "Analiza el tono emocional de tu contenido",
        
        chat_title: "Consultor de IA",
        chat_desc: "Obtén consejos de expertos sobre tu estrategia de marca",
        chat_welcome: "¡Bienvenido al Consultor de IA de BizForge! Pregúntame cualquier cosa sobre tu estrategia de marca.",
        
        form_description: "Descripción del Negocio",
        form_brand_name: "Nombre de la Marca",
        form_text: "Texto para Analizar",
        form_style: "Estilo de Diseño",
        style_modern: "Moderno",
        style_classic: "Clásico",
        style_playful: "Lúdico",
        style_minimal: "Minimalista",
        
        btn_generate: "Generar Nombres",
        btn_generate_logo: "Generar Logo",
        btn_generate_content: "Generar Contenido",
        btn_generate_design: "Generar Paleta",
        btn_analyze: "Analizar",
        btn_send: "Enviar",
        btn_download: "Descargar",
        
        tagline: "Eslogan",
        headline: "Titular",
        description: "Descripción",
        score: "Puntuación",
        explanation: "Análisis",
        
        loading: "Generando...",
        loading_logo: "Generando logo... Esto puede tomar 20-30 segundos"
    },
    
    fr: {
        hero_title: "Génération de Marques Alimentée par l'IA",
        hero_subtitle: "Créez des marques, logos et contenus marketing époustouflants en quelques secondes avec l'IA avancée",
        cta_primary: "Lancer Studio",
        cta_secondary: "En savoir plus",
        
        feature_ai: "🤖 Alimenté par l'IA",
        feature_fast: "⚡ Ultra Rapide",
        feature_multilingual: "🌍 Multilingue",
        features_title: "Caractéristiques Puissantes",
        features_subtitle: "Tout ce dont vous avez besoin pour construire votre marque",
        feature_brand_title: "Noms de Marque",
        feature_brand_desc: "Générez des noms créatifs et mémorables qui résonnent auprès de votre public",
        feature_logo_title: "Conception de Logo",
        feature_logo_desc: "Logos professionnels générés par l'IA utilisant Stable Diffusion XL",
        feature_content_title: "Contenu Marketing",
        feature_content_desc: "Créez des slogans, titres et descriptions convaincants à l'instant",
        feature_color_title: "Palettes de Couleurs",
        feature_color_desc: "Obtenez des schémas de couleurs parfaitement assortis pour votre identité de marque",
        feature_sentiment_title: "Analyse du Sentiment",
        feature_sentiment_desc: "Comprenez le ton émotionnel de vos messages marketing",
        feature_chat_title: "Consultant IA",
        feature_chat_desc: "Obtenez des conseils de stratégie de marque d'experts alimentés par l'IA avancée",
        
        why_title: "Pourquoi Choisir BizForge ?",
        why_subtitle: "Le choix intelligent pour la création de marque",
        why_speed: "Ultra Rapide",
        why_speed_desc: "Obtenez des résultats en quelques secondes, pas en jours",
        why_accuracy: "Précision Alimentée par l'IA",
        why_accuracy_desc: "Algorithmes avancés entraînés sur des millions de marques",
        why_cost: "Abordable",
        why_cost_desc: "Pas de frais de concepteur coûteux ni de coûts d'agence",
        why_global: "Portée Mondiale",
        why_global_desc: "Prise en charge de 5+ langues dans toutes les fonctionnalités",
        why_easy: "Facile à Utiliser",
        why_easy_desc: "Interface intuitive, aucune expérience en conception requise",
        why_iterate: "Itérations Illimitées",
        why_iterate_desc: "Générez des variations jusqu'à trouver la perfection",
        
        footer_tagline: "Plateforme de Génération de Marques Alimentée par l'IA",
        footer_resources: "Ressources",
        footer_launch: "Lancer Studio",
        footer_features: "Caractéristiques",
        footer_docs: "Documentation",
        footer_legal: "Légal",
        footer_privacy: "Politique de Confidentialité",
        footer_terms: "Conditions d'utilisation",
        footer_copyright: "© 2024 BizForge. Tous droits réservés.",
        
        studio_title: "Studio de Marque",
        tab_brand: "Noms de Marque",
        tab_logo: "Conception de Logo",
        tab_content: "Marketing",
        tab_design: "Système de Conception",
        tab_sentiment: "Sentiment",
        tab_chat: "Chat IA",
        
        brand_title: "Générer des Noms de Marque",
        brand_desc: "Obtenez des noms créatifs et mémorables pour votre entreprise",
        
        logo_title: "Générer un Logo",
        logo_desc: "Créez des logos professionnels générés par l'IA pour votre marque",
        
        content_title: "Générer du Contenu Marketing",
        content_desc: "Créez des slogans et des descriptions convaincants",
        
        design_title: "Système de Conception",
        design_desc: "Générez des palettes de couleurs et des directives de conception",
        
        sentiment_title: "Analyse du Sentiment",
        sentiment_desc: "Analysez le ton émotionnel de votre contenu",
        
        chat_title: "Consultant IA",
        chat_desc: "Obtenez des conseils d'experts sur votre stratégie de marque",
        chat_welcome: "Bienvenue au Consultant IA de BizForge ! Posez-moi toute question sur votre stratégie de marque.",
        
        form_description: "Description de l'Entreprise",
        form_brand_name: "Nom de la Marque",
        form_text: "Texte à Analyser",
        form_style: "Style de Conception",
        style_modern: "Moderne",
        style_classic: "Classique",
        style_playful: "Ludique",
        style_minimal: "Minimaliste",
        
        btn_generate: "Générer les Noms",
        btn_generate_logo: "Générer le Logo",
        btn_generate_content: "Générer le Contenu",
        btn_generate_design: "Générer la Palette",
        btn_analyze: "Analyser",
        btn_send: "Envoyer",
        btn_download: "Télécharger",
        
        tagline: "Slogan",
        headline: "Titre",
        description: "Description",
        score: "Score",
        explanation: "Analyse",
        
        loading: "Génération en cours...",
        loading_logo: "Génération du logo... Cela peut prendre 20-30 secondes"
    },
    
    de: {
        hero_title: "KI-gesteuerte Markengenerierung",
        hero_subtitle: "Erstellen Sie mit fortschrittlicher KI in Sekunden atemberaubende Marken, Logos und Marketinginhalte",
        cta_primary: "Studio Starten",
        cta_secondary: "Mehr erfahren",
        
        feature_ai: "🤖 KI-gesteuert",
        feature_fast: "⚡ Blitzschnell",
        feature_multilingual: "🌍 Mehrsprachig",
        features_title: "Leistungsstarke Funktionen",
        features_subtitle: "Alles, was Sie zum Aufbau Ihrer Marke benötigen",
        feature_brand_title: "Markennamen",
        feature_brand_desc: "Generieren Sie kreative, prägnante Namen, die bei Ihrem Publikum ankommen",
        feature_logo_title: "Logodesign",
        feature_logo_desc: "Von der KI generierte professionelle Logos mit Stable Diffusion XL",
        feature_content_title: "Marketinginhalte",
        feature_content_desc: "Erstellen Sie auf der Stelle überzeugende Slogans, Überschriften und Beschreibungen",
        feature_color_title: "Farbpaletten",
        feature_color_desc: "Erhalten Sie perfekt abgestimmte Farbschemen für Ihre Markenidentität",
        feature_sentiment_title: "Sentimentanalyse",
        feature_sentiment_desc: "Verstehen Sie den emotionalen Ton Ihrer Marketingbotschaften",
        feature_chat_title: "KI-Berater",
        feature_chat_desc: "Erhalten Sie Expertenrat zur Markenstrategie mit fortschrittlicher KI",
        
        why_title: "Warum BizForge wählen?",
        why_subtitle: "Die intelligente Wahl für die Markenerstellung",
        why_speed: "Blitzschnell",
        why_speed_desc: "Erhalten Sie in Sekunden Ergebnisse, nicht in Tagen",
        why_accuracy: "KI-gesteuerte Genauigkeit",
        why_accuracy_desc: "Fortgeschrittene Algorithmen, trainiert an Millionen von Marken",
        why_cost: "Erschwinglich",
        why_cost_desc: "Keine teuren Designerhonorare oder Agenturkosten",
        why_global: "Globale Reichweite",
        why_global_desc: "Unterstützung für 5+ Sprachen auf allen Features",
        why_easy: "Einfach zu bedienen",
        why_easy_desc: "Intuitive Oberfläche, keine Designerfahrung erforderlich",
        why_iterate: "Unbegrenzte Iterationen",
        why_iterate_desc: "Generieren Sie Variationen, bis Sie die Perfektion finden",
        
        footer_tagline: "KI-gesteuerte Markengenerierungsplattform",
        footer_resources: "Ressourcen",
        footer_launch: "Studio Starten",
        footer_features: "Funktionen",
        footer_docs: "Dokumentation",
        footer_legal: "Rechtliches",
        footer_privacy: "Datenschutzrichtlinie",
        footer_terms: "Nutzungsbedingungen",
        footer_copyright: "© 2024 BizForge. Alle Rechte vorbehalten.",
        
        studio_title: "Marken-Studio",
        tab_brand: "Markennamen",
        tab_logo: "Logodesign",
        tab_content: "Marketing",
        tab_design: "Design-System",
        tab_sentiment: "Sentiment",
        tab_chat: "KI Chat",
        
        brand_title: "Markennamen generieren",
        brand_desc: "Erhalten Sie kreative, prägnante Namen für Ihr Geschäft",
        
        logo_title: "Logo generieren",
        logo_desc: "Erstellen Sie mit KI generierte professionelle Logos für Ihre Marke",
        
        content_title: "Marketinginhalte generieren",
        content_desc: "Erstellen Sie überzeugende Slogans und Beschreibungen",
        
        design_title: "Design-System",
        design_desc: "Generieren Sie Farbpaletten und Designrichtlinien",
        
        sentiment_title: "Sentimentanalyse",
        sentiment_desc: "Analysieren Sie den emotionalen Ton Ihres Inhalts",
        
        chat_title: "KI-Berater",
        chat_desc: "Erhalten Sie Expertenrat zu Ihrer Markenstrategie",
        chat_welcome: "Willkommen bei BizForge KI-Berater! Stellen Sie mir Fragen zu Ihrer Markenstrategie.",
        
        form_description: "Unternehmensbeschreibung",
        form_brand_name: "Markenname",
        form_text: "Text zum Analysieren",
        form_style: "Design-Stil",
        style_modern: "Modern",
        style_classic: "Klassisch",
        style_playful: "Verspielt",
        style_minimal: "Minimal",
        
        btn_generate: "Namen generieren",
        btn_generate_logo: "Logo generieren",
        btn_generate_content: "Inhalt generieren",
        btn_generate_design: "Palette generieren",
        btn_analyze: "Analysieren",
        btn_send: "Senden",
        btn_download: "Downloaden",
        
        tagline: "Slogan",
        headline: "Überschrift",
        description: "Beschreibung",
        score: "Bewertung",
        explanation: "Analyse",
        
        loading: "Wird generiert...",
        loading_logo: "Logo wird generiert... Dies kann 20-30 Sekunden dauern"
    },
    
    hi: {
        hero_title: "AI-संचालित ब्रांड जनरेशन",
        hero_subtitle: "उन्नत AI के साथ सेकंडों में शानदार ब्रांड, लोगो और मार्केटिंग सामग्री बनाएं",
        cta_primary: "स्टूडियो लॉन्च करें",
        cta_secondary: "और जानें",
        
        feature_ai: "🤖 AI-संचालित",
        feature_fast: "⚡ बिजली तेज",
        feature_multilingual: "🌍 बहुभाषी",
        features_title: "शक्तिशाली विशेषताएं",
        features_subtitle: "अपना ब्रांड बनाने के लिए आपको सभी कुछ चाहिए",
        feature_brand_title: "ब्रांड नाम",
        feature_brand_desc: "रचनात्मक, यादगार नाम बनाएं जो आपके दर्शकों के साथ गूंजते हैं",
        feature_logo_title: "लोगो डिजाइन",
        feature_logo_desc: "Stable Diffusion XL का उपयोग करके AI-जनित पेशेवर लोगो",
        feature_content_title: "विपणन सामग्री",
        feature_content_desc: "तुरंत सम्मोहक टैगलाइनें, हेडलाइनें और विवरण बनाएं",
        feature_color_title: "रंग पैलेट",
        feature_color_desc: "अपनी ब्रांड पहचान के लिए पूरी तरह मेल खाने वाली रंग योजनाएं प्राप्त करें",
        feature_sentiment_title: "भावना विश्लेषण",
        feature_sentiment_desc: "अपने विपणन संदेशों के भावनात्मक स्वर को समझें",
        feature_chat_title: "AI सलाहकार",
        feature_chat_desc: "उन्नत AI द्वारा संचालित ब्रांड रणनीति विशेषज्ञ सलाह प्राप्त करें",
        
        why_title: "BizForge क्यों चुनें?",
        why_subtitle: "ब्रांड निर्माण के लिए स्मार्ट पसंद",
        why_speed: "बिजली तेज",
        why_speed_desc: "दिनों में नहीं, सेकंडों में परिणाम प्राप्त करें",
        why_accuracy: "AI-संचालित सटीकता",
        why_accuracy_desc: "लाखों ब्रांडों पर प्रशिक्षित उन्नत एल्गोरिदम",
        why_cost: "किफायती",
        why_cost_desc: "कोई महंगे डिजाइनर शुल्क या एजेंसी लागत नहीं",
        why_global: "वैश्विक पहुंच",
        why_global_desc: "सभी विशेषताओं में 5+ भाषाओं का समर्थन",
        why_easy: "उपयोग में आसान",
        why_easy_desc: "सहज इंटरफेस, कोई डिजाइन अनुभव आवश्यक नहीं",
        why_iterate: "असीम पुनरावृत्तियाँ",
        why_iterate_desc: "जब तक आप पूर्णता न पा लें तब तक भिन्नताएं बनाएं",
        
        footer_tagline: "AI-संचालित ब्रांड जनरेशन प्लेटफॉर्म",
        footer_resources: "संसाधन",
        footer_launch: "स्टूडियो लॉन्च करें",
        footer_features: "विशेषताएं",
        footer_docs: "प्रलेखन",
        footer_legal: "कानूनी",
        footer_privacy: "गोपनीयता नीति",
        footer_terms: "सेवा की शर्तें",
        footer_copyright: "© 2024 BizForge। सर्वाधिकार सुरक्षित।",
        
        studio_title: "ब्रांड स्टूडियो",
        tab_brand: "ब्रांड नाम",
        tab_logo: "लोगो डिजाइन",
        tab_content: "विपणन",
        tab_design: "डिजाइन सिस्टम",
        tab_sentiment: "भावना",
        tab_chat: "AI चैट",
        
        brand_title: "ब्रांड नाम बनाएं",
        brand_desc: "अपने व्यवसाय के लिए रचनात्मक, यादगार नाम प्राप्त करें",
        
        logo_title: "लोगो बनाएं",
        logo_desc: "अपने ब्रांड के लिए AI-जनित पेशेवर लोगो बनाएं",
        
        content_title: "विपणन सामग्री बनाएं",
        content_desc: "सम्मोहक टैगलाइनें और विवरण बनाएं",
        
        design_title: "डिजाइन सिस्टम",
        design_desc: "रंग पैलेट और डिजाइन दिशानिर्देश बनाएं",
        
        sentiment_title: "भावना विश्लेषण",
        sentiment_desc: "अपनी सामग्री के भावनात्मक स्वर का विश्लेषण करें",
        
        chat_title: "AI सलाहकार",
        chat_desc: "अपनी ब्रांड रणनीति पर विशेषज्ञ सलाह प्राप्त करें",
        chat_welcome: "BizForge AI सलाहकार में आपका स्वागत है! अपनी ब्रांड रणनीति के बारे में मुझसे कुछ भी पूछें।",
        
        form_description: "व्यवसाय विवरण",
        form_brand_name: "ब्रांड का नाम",
        form_text: "विश्लेषण के लिए पाठ",
        form_style: "डिजाइन शैली",
        style_modern: "आधुनिक",
        style_classic: "मास्टर",
        style_playful: "खेल",
        style_minimal: "न्यूनतम",
        
        btn_generate: "नाम बनाएं",
        btn_generate_logo: "लोगो बनाएं",
        btn_generate_content: "सामग्री बनाएं",
        btn_generate_design: "पैलेट बनाएं",
        btn_analyze: "विश्लेषण करें",
        btn_send: "भेजें",
        btn_download: "डाउनलोड करें",
        
        tagline: "टैगलाइन",
        headline: "शीर्षक",
        description: "विवरण",
        score: "स्कोर",
        explanation: "विश्लेषण",
        
        loading: "बनाया जा रहा है...",
        loading_logo: "लोगो बनाया जा रहा है... यह 20-30 सेकंड ले सकता है"
    }
};

// Apply translations to DOM
function applyTranslations(language) {
    const t = translations[language] || translations['en'];
    
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (t[key]) {
            if (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA') {
                element.placeholder = t[key];
            } else if (element.tagName === 'OPTION') {
                element.textContent = t[key];
            } else {
                element.textContent = t[key];
            }
        }
    });
    
    // Update HTML lang attribute
    document.documentElement.lang = language;
    localStorage.setItem('language', language);
}

// Initialize on page load
window.addEventListener('load', () => {
    const savedLanguage = localStorage.getItem('language') || 'en';
    applyTranslations(savedLanguage);
});
