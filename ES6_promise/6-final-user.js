import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]).then((results) =>
    results.map((res) => {
      if (res.status === 'fulfilled') {
        return { status: res.status, value: res.value };
      }

      const msg =
        res.reason instanceof Error ? res.reason.toString() : String(res.reason);
      return { status: res.status, value: msg };
    })
  );
}
