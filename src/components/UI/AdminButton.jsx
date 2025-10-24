import { Link } from "react-router-dom";

export const AdminButton = () => {
  return (
    <Link to="/admin" className="admin-button">
      Admin Panel
    </Link>
  );
};
