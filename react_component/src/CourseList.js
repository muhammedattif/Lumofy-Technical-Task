import React, { useEffect, useState } from 'react';

const CourseList = () => {
  const [courses, setCourses] = useState([]);
  const [nextPage, setNextPage] = useState(null);
  const [previousPage, setPreviousPage] = useState(null);

  const fetchCourses = async (url) => {
    try {
        var options = {
            method: 'GET',
            headers: {
              'Authorization': 'Token e83b7b11b9f02b4ef08401731794338d79efe117',
            }
          }
      const response = await fetch(url, options);
      const data = await response.json();
      setCourses(data.data);
      setNextPage(data.next);
      setPreviousPage(data.previous);
    } catch (error) {
      console.error('Error fetching courses:', error);
    }
  };

  useEffect(() => {
    fetchCourses('http://localhost/api/v1/courses/'); // Replace with your API endpoint
  }, []);

  return (
    <div>
      <h1>Course List</h1>
      <ul>
        {courses.map(course => (
          <li key={course.id}>{course.name}</li>
        ))}
      </ul>
      <div>
        {previousPage && (
          <button onClick={() => fetchCourses(previousPage)}>Previous</button>
        )}
        {nextPage && (
          <button onClick={() => fetchCourses(nextPage)}>Next</button>
        )}
      </div>
    </div>
  );
};

export default CourseList;
