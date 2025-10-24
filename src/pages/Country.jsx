import { useEffect, useState, useTransition } from "react";
import {
  getCountryData,
  searchCountries,
  getCountriesByRegion,
} from "../api/postApi";
import { Loader } from "../components/UI/Loader";
import { CountryCard } from "../components/Layout/CountryCard";
import { SearchFilter } from "../components/UI/SerachFilter";

export const Country = () => {
  const [isPending, startTransition] = useTransition();
  const [countries, setCountries] = useState([]);

  const [search, setSearch] = useState("");
  const [filter, setFilter] = useState("all");

  useEffect(() => {
    startTransition(async () => {
      try {
        const res = await getCountryData();
        setCountries(res.data);
      } catch (error) {
        console.error("Failed to load countries:", error);
        setCountries([]);
      }
    });
  }, []);

  if (isPending) return <Loader />;

  // console.log(search, filter);

  const searchCountry = (country) => {
    if (search) {
      return country.name.common.toLowerCase().includes(search.toLowerCase());
    }
    return country;
  };

  const filterRegion = (country) => {
    if (filter === "all") return country;
    return country.region === filter;
  };

  // Enhanced search with backend API
  useEffect(() => {
    if (search || filter !== "all") {
      startTransition(async () => {
        try {
          const searchParams = {};
          if (search) searchParams.name = search;
          if (filter !== "all") searchParams.region = filter;

          const res = await searchCountries(searchParams);
          setCountries(res.data);
        } catch (error) {
          console.error("Search failed, using local filter:", error);
          // Fallback to local filtering
        }
      });
    }
  }, [search, filter]);

  // here is the main logic (fallback for local filtering)
  const filterCountries = countries.filter(
    (country) => searchCountry(country) && filterRegion(country)
  );

  return (
    <section className="country-section">
      <SearchFilter
        search={search}
        setSearch={setSearch}
        filter={filter}
        setFilter={setFilter}
        countries={countries}
        setCountries={setCountries}
      />

      <ul className="grid grid-four-cols">
        {filterCountries.map((curCountry, index) => {
          return <CountryCard country={curCountry} key={index} />;
        })}
      </ul>
    </section>
  );
};
