import { useState, useEffect } from "react";
import {
  getCountryStats,
  createCountry,
  updateCountry,
  deleteCountry,
} from "../api/postApi";

export const AdminPanel = () => {
  const [stats, setStats] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [editingCountry, setEditingCountry] = useState(null);
  const [formData, setFormData] = useState({
    name: "",
    capital: "",
    population: "",
    region: "",
    subregion: "",
    area: "",
    flag_url: "",
    interesting_fact: "",
    currency: "",
    language: "",
    timezone: "",
    is_independent: true,
  });

  useEffect(() => {
    loadStats();
  }, []);

  const loadStats = async () => {
    try {
      const response = await getCountryStats();
      setStats(response.data);
    } catch (error) {
      console.error("Failed to load statistics:", error);
    }
  };

  const handleInputChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (editingCountry) {
        await updateCountry(editingCountry.id, formData);
        alert("Country updated successfully!");
      } else {
        await createCountry(formData);
        alert("Country created successfully!");
      }
      setFormData({
        name: "",
        capital: "",
        population: "",
        region: "",
        subregion: "",
        area: "",
        flag_url: "",
        interesting_fact: "",
        currency: "",
        language: "",
        timezone: "",
        is_independent: true,
      });
      setShowForm(false);
      setEditingCountry(null);
      loadStats();
    } catch (error) {
      alert("Error: " + error.response?.data?.detail || error.message);
    }
  };

  const handleEdit = (country) => {
    setEditingCountry(country);
    setFormData({
      name: country.name || "",
      capital: country.capital || "",
      population: country.population || "",
      region: country.region || "",
      subregion: country.subregion || "",
      area: country.area || "",
      flag_url: country.flag_url || "",
      interesting_fact: country.interesting_fact || "",
      currency: country.currency || "",
      language: country.language || "",
      timezone: country.timezone || "",
      is_independent: country.is_independent !== false,
    });
    setShowForm(true);
  };

  const handleDelete = async (countryId) => {
    if (window.confirm("Are you sure you want to delete this country?")) {
      try {
        await deleteCountry(countryId);
        alert("Country deleted successfully!");
        loadStats();
      } catch (error) {
        alert("Error: " + error.response?.data?.detail || error.message);
      }
    }
  };

  return (
    <div className="admin-panel">
      <div className="admin-header">
        <h2>Admin Panel</h2>
        <button
          onClick={() => setShowForm(!showForm)}
          className="btn btn-primary"
        >
          {showForm ? "Cancel" : "Add New Country"}
        </button>
      </div>

      {stats && (
        <div className="stats-grid">
          <div className="stat-card">
            <h3>Total Countries</h3>
            <p>{stats.total_countries}</p>
          </div>
          <div className="stat-card">
            <h3>Total Population</h3>
            <p>{stats.total_population?.toLocaleString()}</p>
          </div>
          <div className="stat-card">
            <h3>Average Population</h3>
            <p>{Math.round(stats.average_population)?.toLocaleString()}</p>
          </div>
          <div className="stat-card">
            <h3>Regions</h3>
            <p>{stats.regions?.length}</p>
          </div>
        </div>
      )}

      {showForm && (
        <div className="country-form">
          <h3>{editingCountry ? "Edit Country" : "Add New Country"}</h3>
          <form onSubmit={handleSubmit}>
            <div className="form-grid">
              <div className="form-group">
                <label>Country Name *</label>
                <input
                  type="text"
                  name="name"
                  value={formData.name}
                  onChange={handleInputChange}
                  required
                />
              </div>
              <div className="form-group">
                <label>Capital</label>
                <input
                  type="text"
                  name="capital"
                  value={formData.capital}
                  onChange={handleInputChange}
                />
              </div>
              <div className="form-group">
                <label>Population</label>
                <input
                  type="number"
                  name="population"
                  value={formData.population}
                  onChange={handleInputChange}
                />
              </div>
              <div className="form-group">
                <label>Region</label>
                <select
                  name="region"
                  value={formData.region}
                  onChange={handleInputChange}
                >
                  <option value="">Select Region</option>
                  <option value="Asia">Asia</option>
                  <option value="Europe">Europe</option>
                  <option value="Africa">Africa</option>
                  <option value="Americas">Americas</option>
                  <option value="Oceania">Oceania</option>
                </select>
              </div>
              <div className="form-group">
                <label>Subregion</label>
                <input
                  type="text"
                  name="subregion"
                  value={formData.subregion}
                  onChange={handleInputChange}
                />
              </div>
              <div className="form-group">
                <label>Area (sq km)</label>
                <input
                  type="number"
                  name="area"
                  value={formData.area}
                  onChange={handleInputChange}
                />
              </div>
              <div className="form-group">
                <label>Flag URL</label>
                <input
                  type="url"
                  name="flag_url"
                  value={formData.flag_url}
                  onChange={handleInputChange}
                />
              </div>
              <div className="form-group">
                <label>Currency</label>
                <input
                  type="text"
                  name="currency"
                  value={formData.currency}
                  onChange={handleInputChange}
                />
              </div>
              <div className="form-group">
                <label>Language</label>
                <input
                  type="text"
                  name="language"
                  value={formData.language}
                  onChange={handleInputChange}
                />
              </div>
              <div className="form-group">
                <label>Timezone</label>
                <input
                  type="text"
                  name="timezone"
                  value={formData.timezone}
                  onChange={handleInputChange}
                />
              </div>
              <div className="form-group">
                <label>
                  <input
                    type="checkbox"
                    name="is_independent"
                    checked={formData.is_independent}
                    onChange={handleInputChange}
                  />
                  Independent Country
                </label>
              </div>
            </div>
            <div className="form-group full-width">
              <label>Interesting Fact</label>
              <textarea
                name="interesting_fact"
                value={formData.interesting_fact}
                onChange={handleInputChange}
                rows="3"
              />
            </div>
            <div className="form-actions">
              <button type="submit" className="btn btn-primary">
                {editingCountry ? "Update Country" : "Create Country"}
              </button>
              <button
                type="button"
                onClick={() => {
                  setShowForm(false);
                  setEditingCountry(null);
                }}
                className="btn btn-secondary"
              >
                Cancel
              </button>
            </div>
          </form>
        </div>
      )}
    </div>
  );
};
