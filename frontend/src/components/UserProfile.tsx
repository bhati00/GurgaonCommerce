import React, { useState, useEffect } from 'react';
import { User } from '../common/types';
import { getUser } from '../api/users';


const UserProfile: React.FC = () => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const userData = await getUser();
        setUser(userData);
      } catch (error) {
        setError('Failed to fetch user profile.');
      } finally {
        setLoading(false);
      }
    };

    fetchUser();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <div>
      {user ? (
        <div>
          <h2>{user.email}</h2>
          <p>Email: {user.email}</p>
          {/* Add more user details here as needed */}
        </div>
      ) : (
        <div>No user data available.</div>
      )}
    </div>
  );
};

export default UserProfile;
