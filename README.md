
# Companio: AI-Powered ADA Travel Assistant

## Project Summary for PowerPoint

### 🎯 Project Overview

An AI-driven travel planning system that intelligently searches and recommends ADA-compliant hotels and attractions, generating personalized accessible itineraries for users with disabilities.

---

## Workflow
```mermaid
flowchart TD
    A["User Input: Travel Preferences & Accessibility Needs"] --> B{"AI Agent"}
    B --> C["Dynamic SQL Generation<br/>(Create DB queries for hotels & attractions)"]
    C --> D["Hotel Search<br/>(Filter ADA-compliant hotels)"]
    C --> E["Attraction Search<br/>(Filter accessible attractions)"]
    D --> F["Rank Hotels<br/>(By reviews & accessibility)"]
    E --> G["Rank Attractions<br/>(By ratings & accessibility)"]
    F --> H["Select Top 5 Hotels"]
    G --> I["Select Top 5 Attractions"]
    H --> J["Smart Itinerary Creation<br/>(Combine hotels & attractions)"]
    I --> J
    J --> K["Personalized Accessible Itinerary<br/>(Results with highlighted accessibility features)"]
```

## 🤖 AI Features

- **Dynamic SQL Generation:**  
    AI automatically creates database queries based on user preferences and accessibility needs.

- **Intelligent Recommendations:**  
    Machine learning algorithms rank and select the top 5 hotels/attractions based on ratings and ADA compliance.

- **Smart Itinerary Creation:**  
    AI synthesizes hotel and attraction data into comprehensive, accessible travel plans.

---

## 🏨 AI Agent - Hotel Booking

- Searches ADA-compliant accommodations using keywords: *wheelchair*, *accessible*, *ADA*, *disabled*, *mobility*.
- Filters by location, availability, and accessibility features.
- Ranks hotels by review scores (1-10 scale) and accessibility quality.

---

## 🎭 AI Agent - Attractions

- Identifies tourist attractions with disability accommodations.
- Analyzes `services_provided` field for accessibility features.
- Recommends top-rated accessible attractions by location.

---

## ♿ Disability Search Features

- **Keyword Recognition:**  
    Automatically detects accessibility-related terms in user input.

- **ADA Compliance Filtering:**  
    Searches property highlights and services for wheelchair access, accessible bathrooms, and mobility aids.

- **Personalized Matching:**  
    Matches specific disability needs with appropriate accommodations and attractions.

- **Structured Results:**  
    Displays accessibility features prominently in recommendations.
