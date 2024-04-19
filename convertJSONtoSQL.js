const fs = require('fs');
function jsonToSQL(jsonData, tableName) {
    let sql = `INSERT INTO ${tableName} (id, name, description, district, location, link, latitude, longitude, image_paths) VALUES\n`;

    for (let i = 0; i < jsonData.length; i++) {
        const obj = jsonData[i];
        const imagePaths = obj.imagePaths && obj.imagePaths.length > 0 ? obj.imagePaths.join(';') : '';
        sql += `(${obj.id}, '${obj.name.replace(/'/g, "''")}', '${obj.description.replace(/'/g, "''")}', '${obj.district}', '${obj.location}', '${obj.link}', ${obj.coordinates.latitude}, ${obj.coordinates.longitude}, '${imagePaths}'),\n`;
    }

    sql = sql.slice(0, -2) + ';';

    return sql;
}

const inputFile = 'input.json'; 
const outputFile = 'output.sql';
const tableName = 'your_table';

fs.readFile(inputFile, 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading JSON file:', err);
        return;
    }

    try {
        const jsonData = JSON.parse(data);
        const sql = jsonToSQL(jsonData, tableName);

        fs.writeFile(outputFile, sql, err => {
            if (err) {
                console.error('Error writing SQL file:', err);
                return;
            }
            console.log('SQL file generated successfully!');
        });
    } catch (err) {
        console.error('Error parsing JSON data:', err);
    }
});
