import axios from "axios";

// Backend API configuration
const backendApi = axios.create({
  baseURL: "http://localhost:8000/api/v1",
});

// External API configuration (fallback)
const externalApi = axios.create({
  baseURL: "https://restcountries.com/v3.1",
});

// Backend API methods
export const getCountryData = async (page = 0, limit = 100) => {
  try {
    // Try backend API first
    const response = await backendApi.get(
      `/countries/?skip=${page * limit}&limit=${limit}`
    );
    return response;
  } catch (error) {
    console.warn("Backend API not available, falling back to external API");
    // Fallback to external API
    return externalApi.get("/all?fields=name,population,region,capital,flags");
  }
};

export const getCountryIndData = async (name) => {
  try {
    // Try backend API first
    const response = await backendApi.get(`/countries/name/${name}`);
    return response;
  } catch (error) {
    console.warn("Backend API not available, falling back to external API");
    // Fallback to external API
    return externalApi.get(
      `/name/${name}?fullText=true&fields=name,population,region,subregion,capital,tld,currencies,languages,borders,flags`
    );
  }
};

// New backend-specific API methods
export const searchCountries = async (searchParams) => {
  const params = new URLSearchParams();
  Object.keys(searchParams).forEach((key) => {
    if (searchParams[key] !== null && searchParams[key] !== undefined) {
      params.append(key, searchParams[key]);
    }
  });

  try {
    const response = await backendApi.get(
      `/countries/search?${params.toString()}`
    );
    return response;
  } catch (error) {
    console.error("Search failed:", error);
    throw error;
  }
};

export const getCountriesByRegion = async (region) => {
  try {
    const response = await backendApi.get(`/countries/region/${region}`);
    return response;
  } catch (error) {
    console.error("Failed to get countries by region:", error);
    throw error;
  }
};

export const getCountryStats = async () => {
  try {
    const response = await backendApi.get("/countries/stats/overview");
    return response;
  } catch (error) {
    console.error("Failed to get country statistics:", error);
    throw error;
  }
};

export const createCountry = async (countryData) => {
  try {
    const response = await backendApi.post("/countries/", countryData);
    return response;
  } catch (error) {
    console.error("Failed to create country:", error);
    throw error;
  }
};

export const updateCountry = async (countryId, countryData) => {
  try {
    const response = await backendApi.put(
      `/countries/${countryId}`,
      countryData
    );
    return response;
  } catch (error) {
    console.error("Failed to update country:", error);
    throw error;
  }
};

export const deleteCountry = async (countryId) => {
  try {
    const response = await backendApi.delete(`/countries/${countryId}`);
    return response;
  } catch (error) {
    console.error("Failed to delete country:", error);
    throw error;
  }
};
